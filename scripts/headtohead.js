// Recompute the head-to-head ratings from the chart data inside benchmarks.html
// and write data/headtohead.json for charts/gen_charts.py. Run: node scripts/headtohead.js
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'benchmarks.html'), 'utf8');
const src = html.split('<script>')[1].split('</script>')[0];
const els = {};
global.document = { getElementById: id => els[id] || (els[id] = { innerHTML: '' }), addEventListener() {} };
global.window = global;
eval(src + ';global.__R={ranked,B};');
const { ranked: rank, B: charts } = global.__R;
const groups = { all: charts };
for (const b of charts) (groups[b[0]] = groups[b[0]] || []).push(b);
const out = { checked: new Date().toISOString().slice(0, 10), benchmarks: charts.length, overall: rank(charts, 6), byGroup: {} };
for (const [g, list] of Object.entries(groups)) if (g !== 'all') out.byGroup[g] = rank(list, 2).slice(0, 10);
fs.writeFileSync(path.join(root, 'data', 'headtohead.json'), JSON.stringify(out, null, 1));
console.log('wrote data/headtohead.json —', out.overall.length, 'models ranked overall');
