# OpenClerk

OpenClerk is an early-stage, open-source lead intake and qualification API for small businesses.

The first milestone is deliberately small: accept a lead, validate it, assign a transparent rule-based priority, and store it in SQLite. AI-powered qualification and external integrations are planned only after this core workflow is tested.

## Current status

**Prototype / early development.** This is not a production-ready CRM and does not yet use an LLM.

### Features
- Create leads through a REST API
- Validate required contact and enquiry fields
- Assign `high`, `medium`, or `low` priority using simple, explainable rules
- Store leads in a local SQLite database
- List saved leads
- Automated tests for the qualification rules and API

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the interactive API docs at http://127.0.0.1:8000/docs.

## API

### Create a lead

`POST /leads`

```json
{
  "name": "Ayesha Khan",
  "email": "ayesha@example.com",
  "business": "Example Dental Clinic",
  "message": "I need an appointment for a dental checkup this week."
}
```

The API returns the saved lead and its priority.

### List leads

`GET /leads`

### Health check

`GET /health`

## Qualification rules

The first version uses keyword-based rules, not AI:
- **High:** message contains an urgent or near-term buying signal such as "today", "urgent", "this week", or "ready to book".
- **Medium:** message contains a clear service or pricing enquiry.
- **Low:** everything else.

These rules are intentionally simple and should be improved with tests and real user feedback. Do not use this prototype for emergency triage or other high-stakes decisions.

## Project structure

```text
openclerk/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── qualification.py
├── tests/
│   ├── test_api.py
│   └── test_qualification.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Roadmap

- [x] First lead intake API
- [x] Local SQLite persistence
- [x] Explainable baseline qualification
- [x] Initial automated tests
- [ ] Configurable qualification rules
- [ ] Optional LLM-based enrichment with human review
- [ ] Google Sheets / CRM integrations
- [ ] Deployment guide and contributor documentation

## Contributing

Issues and pull requests are welcome. Please open an issue to discuss larger changes before submitting a pull request. Add or update tests for behavior changes.

## License

MIT. See [LICENSE](LICENSE).
