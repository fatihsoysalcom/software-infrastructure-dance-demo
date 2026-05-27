# Software Infrastructure Dance Demo

This example demonstrates how application code interacts with and is influenced by its underlying system or infrastructure. It's a simple Python HTTP server whose behavior (displayed message, status code, and response time) changes based on environment variables and the presence of a file, illustrating the 'perfect dance' between software and infrastructure.

## Language

`python`

## How to Run

1. Save the code as `app.py`.
2. Run the server: `python app.py`
3. Open your browser to `http://localhost:8000`.

To see system interaction:
- Set environment: `export APP_ENV=production` (then restart `app.py`).
- Create/delete dependency: `touch /tmp/dependency_ok.txt` or `rm /tmp/dependency_ok.txt` (then refresh browser).
- Simulate delay: `export SIMULATE_DELAY=3` (then restart `app.py`).

## Original Article

This example accompanies the Turkish article: [Kod Çalışır, Sistem de Çalışır: Yazılım ve Altyapının Kusursuz Dansı](https://fatihsoysal.com/blog/kod-calisir-sistem-de-calisir-yazilim-ve-altyapinin-kusursuz-dansi/).

## License

MIT — see [LICENSE](LICENSE).
