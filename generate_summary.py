#!/usr/bin/env python3
"""
Generate update summary for GitHub Actions
"""
import json
import sys
import os

def count_tlds():
    """Count TLDs in the JSON file"""
    try:
        with open('data/tld.json', 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                return len(data)
            elif isinstance(data, list):
                return len(data)
            else:
                return 0
    except Exception as e:
        print(f"Error counting TLDs: {e}")
        return 0

def compare_tlds():
    """Compare old and new TLD data"""
    try:
        if not (os.path.exists('data/tld.json.old') and os.path.exists('data/tld.json')):
            return "No comparison data available"
        
        with open('data/tld.json.old', 'r') as f:
            old_data = json.load(f)
        with open('data/tld.json', 'r') as f:
            new_data = json.load(f)
            
        # Handle different data formats
        if isinstance(old_data, dict):
            old_tlds = set(old_data.keys())
        elif isinstance(old_data, list):
            old_tlds = set(item.get('tld', item.get('dm', '')) for item in old_data)
        else:
            old_tlds = set()
            
        if isinstance(new_data, dict):
            new_tlds = set(new_data.keys())
        elif isinstance(new_data, list):
            new_tlds = set(item.get('tld', item.get('dm', '')) for item in new_data)
        else:
            new_tlds = set()
            
        added = new_tlds - old_tlds
        removed = old_tlds - new_tlds
        
        result = []
        
        if added:
            result.append('🆕 **Added TLDs**:')
            for tld in sorted(added)[:20]:  # Show first 20
                result.append(f'  - {tld}')
            if len(added) > 20:
                result.append(f'  - ... and {len(added)-20} more')
            result.append('')
            
        if removed:
            result.append('🗑️ **Removed TLDs**:')
            for tld in sorted(removed)[:20]:  # Show first 20
                result.append(f'  - {tld}')
            if len(removed) > 20:
                result.append(f'  - ... and {len(removed)-20} more')
            result.append('')
            
        if not added and not removed:
            result.append('✅ **No TLD changes, data refreshed**')
            
        return '\n'.join(result)
        
    except Exception as e:
        return f"⚠️ Unable to compare differences: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "count":
        print(count_tlds())
    elif len(sys.argv) > 1 and sys.argv[1] == "compare":
        print(compare_tlds())
    else:
        print("Usage: python generate_summary.py [count|compare]")