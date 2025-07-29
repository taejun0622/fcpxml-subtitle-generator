#!/usr/bin/env python3
"""
Version bumping utility for fcpxml-subtitle-generator
Usage: python bump_version.py [patch|minor|major]
"""
import sys
import tomllib
import re
from pathlib import Path

def bump_version(version_str, bump_type):
    """Bump version based on type"""
    major, minor, patch = map(int, version_str.split('.'))
    
    if bump_type == 'major':
        return f"{major + 1}.0.0"
    elif bump_type == 'minor':
        return f"{major}.{minor + 1}.0"
    elif bump_type == 'patch':
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError("bump_type must be 'major', 'minor', or 'patch'")

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ['patch', 'minor', 'major']:
        print("Usage: python bump_version.py [patch|minor|major]")
        print("  patch: 0.1.1 -> 0.1.2")
        print("  minor: 0.1.1 -> 0.2.0") 
        print("  major: 0.1.1 -> 1.0.0")
        sys.exit(1)
    
    bump_type = sys.argv[1]
    pyproject_path = Path('pyproject.toml')
    
    if not pyproject_path.exists():
        print("❌ pyproject.toml not found!")
        sys.exit(1)
    
    # Read current version
    with open(pyproject_path, 'rb') as f:
        data = tomllib.load(f)
    
    current_version = data['project']['version']
    new_version = bump_version(current_version, bump_type)
    
    # Update pyproject.toml
    content = pyproject_path.read_text(encoding='utf-8')
    updated_content = re.sub(
        rf'^version = "{re.escape(current_version)}"',
        f'version = "{new_version}"',
        content,
        flags=re.MULTILINE
    )
    
    pyproject_path.write_text(updated_content, encoding='utf-8')
    
    print(f"✅ Version bumped: {current_version} -> {new_version}")
    print(f"📝 Updated pyproject.toml")
    print(f"🚀 Commit and push to trigger auto-deployment:")
    print(f"   git add pyproject.toml")
    print(f"   git commit -m \"Bump version to {new_version}\"")
    print(f"   git push origin main")

if __name__ == '__main__':
    main() 