import requests
import os
import hashlib
from urllib.parse import urlparse

def download_image(url, folder="Fetched_Images", seen_hashes=None, max_size=10*1024*1024):
    """
    Download a single image from the given URL into the folder.
    - Prevents duplicate content using MD5 hashes
    - Skips non-image content
    - Avoids overwriting existing files
    - Set the max_size limit (default 10 MB)
    """
    try:
        # Fetch image (stream for efficiency with large files)
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Check content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Not an image: {url}")
            return {"url": url, "status": "failed", "error": "Not an image"}

        # Check content length before downloading fully
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > max_size:
            print(f"✗ Skipped (too large > {max_size//1024//1024}MB): {url}")
            return {"url": url, "status": "failed", "error": "File too large"}

        # Extract filename from URL or fallback
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

        # Prevent overwriting if filename exists
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(os.path.join(folder, filename)):
            filename = f"{base}_{counter}{ext}"
            counter += 1

        # Get file content
        file_content = response.content

        # Duplicate check using MD5
        file_hash = hashlib.md5(file_content).hexdigest()
        if seen_hashes is not None:
            if file_hash in seen_hashes:
                print(f"⚠ Skipped duplicate: {url}")
                return {"url": url, "status": "skipped", "error": "Duplicate image"}
            seen_hashes.add(file_hash)

        # Save image
        filepath = os.path.join(folder, filename)
        with open(filepath, "wb") as f:
            f.write(file_content)

        print(f"✓ Successfully fetched: {filename}")
        return {"url": url, "status": "success", "filename": filename}

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
        return {"url": url, "status": "failed", "error": str(e)}
    except Exception as e:
        print(f"✗ Unexpected error for {url}: {e}")
        return {"url": url, "status": "failed", "error": str(e)}


def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("Paste multiple image URLs separated by commas or spaces\n")

    # Ensure folder exists
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    # Get URLs from input
    urls = input("Enter image URLs: ")
    urls = [u.strip() for u in urls.replace(",", " ").split() if u.strip()]

    if not urls:
        print("✗ No URLs provided. Exiting.")
        return

    # Remove duplicates and validate
    cleaned_urls = []
    for url in urls:
        if not url.startswith(("http://", "https://")):
            print(f"⚠ Skipping invalid URL (missing scheme): {url}")
        elif url not in cleaned_urls:
            cleaned_urls.append(url)

    if not cleaned_urls:
        print("✗ No valid URLs to process. Exiting.")
        return

    # Track seen file hashes
    seen_hashes = set()

    # Download each
    results = []
    for idx, url in enumerate(cleaned_urls, 1):
        print(f"({idx}/{len(cleaned_urls)}) Downloading: {url}")
        results.append(download_image(url, folder, seen_hashes))

    # Summary
    successes = [r for r in results if r["status"] == "success"]
    skipped = [r for r in results if r["status"] == "skipped"]
    failures = [r for r in results if r["status"] == "failed"]

    print("\n--- Summary ---")
    print(f"✓ {len(successes)} images downloaded successfully")
    print(f"⚠ {len(skipped)} duplicates skipped")
    print(f"✗ {len(failures)} failed")

    if successes:
        print("\nDownloaded files:")
        for s in successes:
            print(f"  - {s['filename']}")

    if skipped:
        print("\nSkipped duplicates:")
        for s in skipped:
            print(f"  - {s['url']}")

    if failures:
        print("\nFailed downloads:")
        for f in failures:
            print(f"  - {f['url']} ({f['error']})")

    print("\nConnection strengthened. Community enriched. 🌱")


if __name__ == "__main__":
    main()
