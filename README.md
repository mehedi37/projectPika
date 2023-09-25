# projectPika

<b><u>_Getting Started :_</u></b>

- `git clone https://github.com/mehedi37/projectPika`
- `cd projectPika`
- create `.env` file here
- Fill the `.env` according to `sample.env.txt`
- For adding class routine from google sheets
  - Visit [google console](https://console.cloud.google.com/)
  - Create a new project and add Google Sheets API to the project
  - Now get your OAuth json file. <i>(Search For how to get, if you have no clue what is this !)</i>
  - Update `SHEET_JSON` in `.env`, where you placed your credentials.json
- Fill other `Environment Variables` as defined
- Make sure you have `python3` in your machine.Use `python --version`
- run `pip install -r requirements.txt --user`
- After successful install, run `python main.py`