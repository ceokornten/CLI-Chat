import express from 'express';

const app = express();
app.use(express.json());

app.get('/', (req, res) => {
  res.json({ status: 'Vault backend running' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server listening on ${PORT}`));
