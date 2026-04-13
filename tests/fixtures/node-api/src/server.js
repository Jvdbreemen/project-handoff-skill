import express from 'express';

const app = express();
const port = process.env.PORT || 3000;
const apiKey = process.env.API_KEY;
const dbUrl = process.env.DATABASE_URL;

if (!apiKey) {
  console.error('API_KEY env var is required');
  process.exit(1);
}

app.get('/health', (req, res) => {
  res.json({ ok: true, db: dbUrl ? 'configured' : 'missing' });
});

app.listen(port, () => {
  console.log(`listening on ${port}`);
});
