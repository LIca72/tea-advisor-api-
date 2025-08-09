# Tea Advisor API (Flask)

A simple REST API built with Flask that:
- Returns a random tea
- Lets you add new teas
- Suggests teas based on mood

Beginner-friendly example of REST API development with basic validation.

---

## 🚀 Quick Start
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python app.py
# tea-advisor-api-
📌 Endpoints
| Method + Path               | Description                                                     |
| --------------------------- | --------------------------------------------------------------- |
| `GET /tea`                  | Returns a random tea from the list                              |
| `POST /tea`                 | Adds a new tea (JSON: `{"name": "Matcha"}`)                     |
| `GET /tea-by-mood?mood=<m>` | Suggests tea based on mood (`relaxed`, `energetic`, `creative`) |

🧪 Curl Examples
# Get a random tea
curl -X GET http://127.0.0.1:5004/tea

# Add a new tea
curl -X POST http://127.0.0.1:5004/tea \
  -H "Content-Type: application/json" \
  -d '{"name":"Matcha"}'

# Get tea by mood (relaxed)
curl -X GET "http://127.0.0.1:5004/tea-by-mood?mood=relaxed"

# Error: empty tea name (400)
curl -X POST http://127.0.0.1:5004/tea \
  -H "Content-Type: application/json" \
  -d '{"name":""}'

# Error: duplicate tea (409)
curl -X POST http://127.0.0.1:5004/tea \
  -H "Content-Type: application/json" \
  -d '{"name":"Matcha"}'

