#!/usr/bin/env python3

"""moroccan-nlp v1.0.0 Upload - PyPI"""

import requests
import hashlib
import os
import glob
import sys


print("="*60)
print("🇲🇦 moroccan-nlp v1.0.0 Upload - PyPI")
print("="*60)
print("Linguistic Resources and Models for Moroccan Darija and Arabic")
print("GITDEEPER LAB ZERO V6 · Series")
print("="*60)

# قراءة README.md
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    print(f"\n📄 README.md: {len(readme)} characters")
except FileNotFoundError:
    print("\n⚠️ README.md not found, using fallback description")
    readme = "moroccan-nlp: Linguistic Resources and Models for Moroccan Darija and Arabic — Building Moroccan AI, one word at a time."

# البحث عن ملفات التوزيع
wheel_files = glob.glob("dist/*.whl")
tar_files = glob.glob("dist/*.tar.gz")

if not wheel_files and not tar_files:
    print("\n📦 No distribution files found. Building package...")
    os.system("python -m build")
    wheel_files = glob.glob("dist/*.whl")
    tar_files = glob.glob("dist/*.tar.gz")

if not wheel_files and not tar_files:
    print("\n❌ No distribution files found. Please run: python -m build")
    sys.exit(1)

print(f"\n📦 Distribution files:")
for f in wheel_files + tar_files:
    print(f"   • {os.path.basename(f)}")

upload_success = False

for filepath in wheel_files + tar_files:
    filename = os.path.basename(filepath)
    print(f"\n📤 Uploading: {filename}")

    # تحديد نوع الملف
    if filename.endswith('.tar.gz'):
        filetype = 'sdist'
        pyversion = 'source'
    else:
        filetype = 'bdist_wheel'
        pyversion = 'py3'

    # حساب الهاشات
    with open(filepath, 'rb') as f:
        content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    # بيانات الرفع - باستخدام project_urls كسلسلة نصية
    data = {
        ':action': 'file_upload',
        'metadata_version': '2.1',
        'name': 'moroccan-nlp',
        'version': '1.0.0',
        'filetype': filetype,
        'pyversion': pyversion,
        'md5_digest': md5_hash,
        'sha256_digest': sha256_hash,
        'description': readme,
        'description_content_type': 'text/markdown',
        'author': 'Samir Baladi',
        'author_email': 'gitdeeper@gmail.com',
        'license': 'MIT',
        'summary': 'Linguistic Resources and Models for Moroccan Darija and Arabic — Building Moroccan AI, one word at a time.',
        'home_page': 'https://moroccan-nlp.netlify.app',
        'requires_python': '>=3.11',
        'keywords': 'morocco, darija, arabic, nlp, natural-language-processing, darijabert, atlas-chat, linguistic-resources, ai, machine-learning',
        'project_urls': 'Documentation, https://moroccan-nlp.netlify.app/documentation, Source, https://github.com/gitdeeper13/moroccan_nlp, DOI, https://doi.org/10.5281/zenodo.21154423'
    }

    # رفع الملف
    try:
        with open(filepath, 'rb') as f:
            response = requests.post(
                'https://upload.pypi.org/legacy/',
                files={'content': (filename, f, 'application/octet-stream')},
                data=data,
                auth=('__token__', TOKEN),
                timeout=120,
                headers={'User-Agent': 'moroccan-nlp-Uploader/1.0.0'}
            )

        print(f"   Status: {response.status_code}")

        if response.status_code in [200, 201]:
            print("   ✅✅✅ SUCCESS!")
            upload_success = True
        else:
            print(f"   ❌ Error: {response.text[:500]}")
    except Exception as e:
        print(f"   ❌ Exception: {str(e)}")

print("\n" + "="*60)
if upload_success:
    print("✅ moroccan-nlp v1.0.0 uploaded successfully!")
    print("🔗 https://pypi.org/project/moroccan-nlp/1.0.0/")
else:
    print("⚠️ Upload completed with some issues.")
    print("🔗 https://pypi.org/project/moroccan-nlp/")
print("="*60)

print("\n📦 Install moroccan-nlp:")
print("   pip install moroccan-nlp")
print("")
print("📖 Documentation:")
print("   https://moroccan-nlp.netlify.app")
print("")
print("📊 Dashboard:")
print("   https://moroccan-nlp.netlify.app/dashboard")
print("")
print("💬 Chat:")
print("   https://moroccan-nlp.netlify.app/chat")
