# SneakerBot-App

A simple GUI-based sneaker bot for Foot Locker release dates.

## What it does
SneakerBot-App is a Python-based tool that automates the process of finding and adding sneakers to a Foot Locker shopping cart. It uses a Tkinter interface to gather product details like model, color, and size, then utilizes Selenium to navigate the Foot Locker release calendar and perform the add-to-cart action.

## Stack
| Component | Detail |
|---|---|
| Language | Python |
| Key libraries | selenium, tkinter |
| Port / endpoint | N/A |

## Quick Start
```bash
# Install dependencies
pip install selenium

# Ensure you have Chrome and ChromeDriver installed and in your PATH.

# Run the bot
python FLBot.py
```

## Environment Variables (if any)
| Variable | Default | Description |
|---|---|---|
| N/A | N/A | N/A |

## API / Usage (if applicable)
```bash
# Launch the application
python FLBot.py

# 1. Enter the Model name in the GUI.
# 2. Enter the Colorway.
# 3. Enter the Size (e.g., 08.0).
# 4. Click 'Go' to start the automation.
```
