import pdfkit
import markdown
import argparse
import requests

def markdown_to_pdf(md_text):
    html = markdown.markdown(md_text)
    with open("temp.html", "w") as file:
      file.write(html)
    pdfkit.from_string(html, "temp.pdf")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help='The link to the markdown file')
    args = parser.parse_args()
    
    md_text = requests.get(args.url).text
    markdown_to_pdf(md_text)

if __name__ == "__main__":
    main()