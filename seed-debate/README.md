# seed-debate

Adds a list of comments in a CSV file to the debate. Saves having to do this one-by-one in the UI.

## Instructions

* Setup your evironment according to the [root README](../README.md)
* Create a CSV file that has at least the following column

| `new-comments` |
| --- |
| _A statement_ |
| _Another statement_ |
| _..._ |

* Copy `.template.env` to `.env` and fill in the relevant details
* Run `python run.py`