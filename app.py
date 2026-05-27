import http.server
import socketserver
import os
import time

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # --- CODE LOGIC PART ---
        # This is the application logic defined in the code itself.
        # It determines the base response to requests.
        status_message = "Application code is running smoothly."
        response_color = "green"
        delay_seconds = 0

        # --- SYSTEM INTERACTION PART ---
        # The code interacts with its environment (the "system")
        # to adapt its behavior or report status, demonstrating the 'dance'.

        # 1. Environment Variable Check (System Configuration)
        # The system's environment variables dictate application behavior.
        # This shows how infrastructure configuration influences software.
        app_env = os.environ.get("APP_ENV", "development")
        if app_env == "production":
            status_message += f" (Environment: {app_env.upper()})";
            response_color = "blue"
        else:
            status_message += f" (Environment: {app_env.capitalize()})";

        # 2. External Dependency Check (System State/Resources)
        # The code checks for an external resource/dependency provided by the system.
        # A missing dependency highlights a system-level issue affecting the code.
        dependency_file = "/tmp/dependency_ok.txt"
        if not os.path.exists(dependency_file):
            status_message += "<br><b>WARNING: Critical system dependency missing!</b>"
            response_color = "orange"
            self.send_response(500) # Indicate a server error due to system issue
        else:
            status_message += "<br>System dependency '/tmp/dependency_ok.txt' is present."
            self.send_response(200) # OK

        # 3. Simulated System Load/Delay (System Performance/Optimization)
        # The system might introduce delays or resource constraints.
        # This simulates a system-level delay affecting code execution time.
        try:
            delay_seconds = int(os.environ.get("SIMULATE_DELAY", "0"))
            if delay_seconds > 0:
                status_message += f"<br>Simulating system delay of {delay_seconds} seconds..."
                time.sleep(delay_seconds) # Simulate a slow system response
        except ValueError:
            pass # Ignore invalid delay values

        # --- RESPONSE GENERATION (Code Output) ---
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Software & Infrastructure Dance</title>
            <style>
                body {{ font-family: sans-serif; margin: 50px; background-color: #f4f4f4; color: #333; }}
                .container {{ background-color: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); max-width: 800px; margin: auto; }}
                h1 {{ color: #0056b3; text-align: center; }}
                p {{ font-size: 1.1em; line-height: 1.6; }}
                .status {{ padding: 15px; border-radius: 5px; margin-top: 20px; font-weight: bold; text-align: center; }}
                .status.green {{ background-color: #e6ffe6; border: 1px solid #00cc00; color: #008000; }}
                .status.blue {{ background-color: #e6f7ff; border: 1px solid #007bff; color: #0056b3; }}
                .status.orange {{ background-color: #fff3e6; border: 1px solid #ff9900; color: #cc6600; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Kod Çalışır, Sistem de Çalışır!</h1>
                <p>Yazılım ve altyapının uyumlu dansını gösteren basit bir örnek.</p>
                <div class="status {response_color}">
                    {status_message}
                    <p>Current Server Time: {time.ctime()}</p>
                </div>
                <p>Bu örnek, uygulamanın (kodun) davranışının, ortam değişkenleri ve dosya sistemi gibi altyapı (sistem) faktörlerinden nasıl etkilendiğini göstermektedir. Kodun tek başına değil, onu destekleyen sistemle birleştiğinde gerçek potansiyeline ulaştığını vurgular.</p>
            </div>
        </body>
        </html>
        """
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(html_content.encode('utf-8'))))
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

# --- SERVER INFRASTRUCTURE PART ---
# This part sets up the "system" (the server process) that runs the code.
# It's the foundation upon which the application code operates.
with socketserver.TCPServer(('', PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    print(f"Access it at http://localhost:{PORT}")
    print("\nTo demonstrate system interaction, try these steps (refresh browser after each):")
    print(f"1. Change environment: export APP_ENV=production (then restart server)")
    print(f"2. Create/delete dependency: touch {dependency_file} / rm {dependency_file}")
    print(f"3. Simulate delay: export SIMULATE_DELAY=3 (then restart server)")
    print("\nRemember to restart the server after changing environment variables.")
    httpd.serve_forever()
