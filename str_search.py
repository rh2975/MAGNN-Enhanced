import os

def search_string_excluding_dirs(directory, search_string, exclude_dirs):
    """Search for string while excluding specific directories"""
    results = []
    exclude_dirs = set(exclude_dirs)  # Convert to set for faster lookup
    
    for root, dirs, files in os.walk(directory):
        # Remove excluded directories from the dirs list to prevent walking into them
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Check if current root contains any excluded directory
        if any(excluded in root for excluded in exclude_dirs):
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if search_string in content:
                        results.append(file_path)
            except (UnicodeDecodeError, PermissionError, IsADirectoryError):
                continue
    
    return results

# Usage - exclude venv directory
exclude_directories = ['magnvenv', 'venv', '.venv', '__pycache__']
found_files = search_string_excluding_dirs('.', 'multivariate-time-series-data', exclude_directories)

print(f"Found in {len(found_files)} files (excluding venv):")
for file_path in found_files:
    print(f"  - {file_path}")