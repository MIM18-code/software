import { marked } from 'marked';
import { copyFileSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const escape = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const apps = [{ slug: 'cold-open', name: 'Cold Open', bundle: 'ColdOpen-user-guide.zip' }, { slug: 'backlot', name: 'Backlot', bundle: 'Backlot-user-guide.zip' }];
function files(dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap(entry => entry.isDirectory() ? files(path.join(dir, entry.name)) : [path.join(dir, entry.name)]);
}
for (const app of apps) {
  const dir = path.join(root, 'guides', app.slug);
  copyFileSync(path.join(root, 'guides/guide.css'), path.join(dir, 'guide.css'));
  const pages = files(dir).filter(file => file.endsWith('.md'));
  const titles = new Map(pages.map(file => [file, readFileSync(file, 'utf8').match(/^# (.+)$/m)?.[1] ?? path.basename(file)]));
  for (const file of pages) {
    const relative = target => path.relative(path.dirname(file), target).split(path.sep).join('/');
    const seen = new Map();
    const renderer = new marked.Renderer();
    renderer.heading = function ({ tokens, depth }) {
      const text = this.parser.parseInline(tokens);
      const base = text.replace(/<[^>]*>/g, '').replace(/&amp;/g, '&').toLowerCase().replace(/[^\p{L}\p{N}_\- ]/gu, '').replaceAll(' ', '-');
      const count = seen.get(base) ?? 0;
      seen.set(base, count + 1);
      return `<h${depth} id="${escape(base + (count ? '-' + count : ''))}">${text}</h${depth}>\n`;
    };
    const source = readFileSync(file, 'utf8');
    let body = marked.parse(source, { renderer });
    body = body.replace(/href="([^"#?]*?)\.md([#?][^"]*)?"/g, (_, href, suffix = '') => `href="${href}${/^(?:[a-z]+:|\/\/)/i.test(href) ? '.md' : '.html'}${suffix}"`);
    let videos = '';
    if (path.relative(dir, file) === 'videos/index.md') {
      videos = '<h2 id="watch-the-walkthroughs">Watch the walkthroughs</h2>' + files(path.join(dir, 'videos')).filter(p => p.endsWith('.mp4')).map(video => {
        const slug = path.basename(video, '.mp4');
        const srt = readFileSync(video.replace(/\.mp4$/, '.srt'), 'utf8');
        writeFileSync(video.replace(/\.mp4$/, '.vtt'), 'WEBVTT\n\n' + srt.replace(/(\d{2}:\d{2}:\d{2}),(\d{3})/g, '$1.$2').replace(/\{\\an\d\}/g, ''));
        const title = readFileSync(video.replace(/\.mp4$/, '.narration-draft.txt'), 'utf8').split('\n')[0].replace(/\.$/, '');
        const transcript = srt.trim().split(/\n\s*\n/).map(cue => `<p>${escape(cue.split('\n').slice(2).join(' ').replace(/\{\\an\d\}/g, ''))}</p>`).join('');
        return `<section class="walkthrough"><h3>${escape(title)}</h3><video controls playsinline preload="metadata" aria-label="${escape(title)}"><source src="${escape(slug)}.mp4" type="video/mp4"><track kind="captions" src="${escape(slug)}.vtt" srclang="en" label="English">Download the video using the links above.</video><p>Captions are visible in the video. <a href="${escape(slug)}.mp4" download>Download video</a></p><details><summary>Read the captions</summary>${transcript}</details></section>`;
      }).join('');
    }
    const navigation = pages.filter(p => path.dirname(p) === dir && path.basename(p) !== 'index.md').map(p => `<li><a${p === file ? ' aria-current="page"' : ''} href="${escape(relative(p).replace(/\.md$/, '.html'))}">${escape(titles.get(p))}</a></li>`).join('');
    writeFileSync(file.replace(/\.md$/, '.html'), `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${escape(titles.get(file))} · ${app.name}</title><link rel="stylesheet" href="${escape(relative(path.join(dir, 'guide.css')))}"></head>
<body><a class="skip" href="#content">Skip to content</a><header><a class="brand" href="${escape(relative(path.join(dir, 'index.html')))}">${app.name} user guide</a><a href="https://mindinmotionsoftware.com/#${app.slug}">Get ${app.name}</a><a href="https://mindinmotionsoftware.com/downloads/${app.bundle}" download>Download complete guide</a></header><div class="layout"><nav aria-label="Guide pages"><details><summary>Guide pages</summary><ul><li><a href="${escape(relative(path.join(dir, 'index.html')))}">Guide home</a></li>${navigation}<li><a href="${escape(relative(path.join(dir, 'videos/index.html')))}">Video walkthroughs</a></li></ul></details></nav><main id="content">${body}${videos}<footer>MindInMotion LLC. Beta software; the guide identifies differences between released and newer screens. <a href="${escape(relative(path.join(dir, 'LICENSE.txt')))}">Guide license</a>.</footer></main></div></body></html>\n`);
  }
  console.log(`${app.name}: ${pages.length} pages`);
}
