# Madhacks-2025-TDS-Workshop
Files for haproxy load balancing demo

# Required Python packages
gunicorn
flask

# Required software
haproxy (`apt install haproxy` for Ubuntu)

# Install
git clone https://github.com/cmusinsky/Madhacks-2025-TDS-Workshop.git
cd Madhacks-2025-TDS-Workshop
gunicorn -w 1 -b 127.0.0.1:9000 slow_app:app

In another terminal:
gunicorn -w 1 -b 127.0.0.1:9001 fast_app:app

And in another terminal:
haproxy -f /etc/haproxy/haproxy.cfg

# Test the server
curl http://localhost:8000
While that's running, open a new terminal and test again!

# Apply to our Infrastructure internship!
https://external-telecom-teldta.icims.com/jobs/28308/infrastructure-intern/job?mode=view
