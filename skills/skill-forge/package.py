#!/usr/bin/env python3
"""Package a skill folder into an installable .skill file.

Usage: python scripts/package.py <skill-folder-path> [output-dir]

Validates the skill structure, then creates a .skill (zip) file.
Output defaults to /mnt/user-data/outputs/
"""

import sys
import os
import zipfile
import re

def validate_skill(skill_path):
    """Validate skill folder has required structure."""
    errors = []
    warnings = []
    
    # Check SKILL.md exists
    skill_md = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_md):
        errors.append("SKILL.md not found (required)")
        return errors, warnings
    
    # Read SKILL.md
    with open(skill_md, 'r') as f:
        content = f.read()
    
    # Check frontmatter
    if not content.startswith('---'):
        errors.append("SKILL.md missing YAML frontmatter (must start with ---)")
    else:
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            frontmatter = fm_match.group(1)
            if 'name:' not in frontmatter:
                errors.append("Frontmatter missing 'name' field")
            if 'description:' not in frontmatter:
                errors.append("Frontmatter missing 'description' field")
            
            # Check description length
            desc_match = re.search(r'description:\s*(.*?)(?=\n\w|\n---|\Z)', frontmatter, re.DOTALL)
            if desc_match:
                desc = desc_match.group(1).strip()
                word_count = len(desc.split())
                if word_count > 200:
                    warnings.append(f"Description is {word_count} words (target: <200)")
                if word_count < 20:
                    warnings.append(f"Description is only {word_count} words (might under-trigger)")
        else:
            errors.append("SKILL.md frontmatter not properly closed (missing second ---)")
    
    # Check line count
    line_count = len(content.split('\n'))
    if line_count > 500:
        warnings.append(f"SKILL.md is {line_count} lines (target: <500). Consider using references/")
    
    # Check references
    refs_dir = os.path.join(skill_path, "references")
    if os.path.exists(refs_dir):
        for ref_file in os.listdir(refs_dir):
            ref_path = os.path.join(refs_dir, ref_file)
            if os.path.isfile(ref_path):
                with open(ref_path, 'r') as f:
                    ref_lines = len(f.read().split('\n'))
                if ref_lines > 300:
                    warnings.append(f"references/{ref_file} is {ref_lines} lines (target: <300)")
    
    return errors, warnings

def package_skill(skill_path, output_dir="/mnt/user-data/outputs"):
    """Package skill folder into .skill zip file."""
    skill_name = os.path.basename(os.path.normpath(skill_path))
    
    # Validate
    errors, warnings = validate_skill(skill_path)
    
    if errors:
        print("ERRORS (must fix):")
        for e in errors:
            print(f"  x {e}")
        return False
    
    if warnings:
        print("WARNINGS (consider fixing):")
        for w in warnings:
            print(f"  ! {w}")
    
    # Package
    output_path = os.path.join(output_dir, f"{skill_name}.skill")
    os.makedirs(output_dir, exist_ok=True)
    
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(skill_path):
            # Skip hidden dirs and __pycache__
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            for file in files:
                if file.startswith('.'):
                    continue
                file_path = os.path.join(root, file)
                arc_name = os.path.join(skill_name, os.path.relpath(file_path, skill_path))
                zf.write(file_path, arc_name)
    
    # Summary
    file_count = sum(len(files) for _, _, files in os.walk(skill_path))
    size_kb = os.path.getsize(output_path) / 1024
    
    print(f"\nPackaged: {output_path}")
    print(f"  {file_count} files, {size_kb:.1f} KB")
    print(f"  Install: extract to your skills directory")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python package.py <skill-folder> [output-dir]")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "/mnt/user-data/outputs"
    
    if not os.path.exists(skill_path):
        print(f"Skill folder not found: {skill_path}")
        sys.exit(1)
    
    success = package_skill(skill_path, output_dir)
    sys.exit(0 if success else 1)
