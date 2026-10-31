<script>
/* A4 쪽 나누기: 왼쪽 단 → 오른쪽 단 → 다음 쪽, 쪽 번호 n / 전체 */
(function () {
  function build() {
    var main = document.querySelector('main'); if (!main || document.querySelector('.sheets')) return;
    var secs = [].slice.call(main.querySelectorAll('section.page'));
    var out = document.createElement('div'); out.className = 'sheets'; main.appendChild(out);
    var pages = [];
    secs.forEach(function (sec) {
      var box = sec.querySelector('.qs, .exp'); if (!box) return;
      var items = [].slice.call(box.children), foot = sec.querySelector('.foot'), top = sec.querySelector('.top');
      var head = [].slice.call(sec.children).filter(function (e) { return e !== box && e !== foot && !(e.classList.contains('keygrid') && false); });
      var cols, ci, first = true;
      function newPage() {
        var pg = document.createElement('div'); pg.className = 'sheet';
        if (first) head.forEach(function (e) { pg.appendChild(e); });
        else { var t = top.cloneNode(true); t.classList.add('run'); pg.appendChild(t); }
        first = false;
        cols = document.createElement('div'); cols.className = 'cols';
        for (var i = 0; i < 2; i++) { var c = document.createElement('div'); c.className = 'col ' + box.className; cols.appendChild(c); }
        pg.appendChild(cols);
        var f = foot.cloneNode(true), sp = f.querySelectorAll('span'), mid = document.createElement('span'); mid.className = 'pno';
        f.insertBefore(mid, sp[1] || null); pg.appendChild(f);
        out.appendChild(pg); pages.push(pg); ci = 0;
      }
      function over(c) { return c.scrollHeight > c.clientHeight + 1; }
      newPage();
      items.forEach(function (it) {
        var c = cols.children[ci]; c.appendChild(it);
        if (over(c) && c.children.length > 1) {
          c.removeChild(it); ci++;
          if (ci > 1) newPage();
          cols.children[ci].appendChild(it);
        }
      });
      sec.parentNode.removeChild(sec);
    });
    pages.forEach(function (p, i) { p.querySelector('.pno').textContent = (i + 1) + ' / ' + pages.length; });
    fit();
  }
  function fit() {
    var w = document.documentElement.clientWidth - 24, s = Math.min(1, w / 794);
    [].forEach.call(document.querySelectorAll('.sheet'), function (p) { p.style.zoom = s < 1 ? s : ''; });
  }
  function go() { (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(build, build); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
  window.addEventListener('resize', function () { if (document.querySelector('.sheets')) fit(); });
})();
</script>
