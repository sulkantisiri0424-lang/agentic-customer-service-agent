
# 🤖 Agentic AI Customer Service Agent

An intelligent customer service application built with Python and Streamlit. It helps customers track orders, check refund status, and find answers to frequently asked questions.

## 🚀 Features

- 📦 Order status tracking
- 💰 Refund status checking
- 📚 FAQ search
- 💬 Interactive chat interface
- 🛠️ Tool-based task execution
- 🗂️ JSON-based demo order database
- 🧠 Intent detection and decision logic

## 🛠️ Technologies Used

- Python
- Streamlit
- JSON
- Regular Expressions
- Git and GitHub

## 🏗️ Project Structure

```text
agentic-customer-service-agent/
├── app.py
├── agent.py
├── tools.py
├── requirements.txt
├── README.md
└── data/
    ├── orders.json
    └── faq.json
```

## ⚙️ How It Works

1. A customer enters a question.
2. The agent identifies the type of request.
3. It selects the appropriate tool.
4. The tool retrieves information from the JSON data.
5. The agent generates a response.

## ▶️ Run Locally

Install Python, then run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Example Questions

- Track order 1001
- Check refund for order 1003
- What is your return policy?
- Can I cancel my order?

## 📌 Project Status

Initial prototype. Uses rule-based intent detection and tool functions. An LLM-powered agent and additional customer service workflows can be added in future versions.

## ⚠️ Disclaimer

This project uses fictional sample customer and order data for demonstration purposes. It is not connected to a real store or payment system.

## 👩‍💻 Author

Created as a learning project to explore AI agents, Python, and customer service automation.
