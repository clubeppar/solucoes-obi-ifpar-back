from dotenv import load_dotenv
import os

try:
    from scripts import update_urls, download_answers
except ModuleNotFoundError:
    import update_urls, download_answers

load_dotenv()

def main():
    years = set(os.getenv("OBI_DEFAULT_YEARS", "2025,2024,2023").split(","))
    update_urls.main(years)
    download_answers.main(years)

if __name__ == "__main__":
    main()
