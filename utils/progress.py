def print_progress(total, completed, new_line=False):
    if not new_line:
        print(f'progress: {int((completed / total) * 100)}%', end='\r')
    else:
        print(f'progress: {int((completed / total) * 100)}%')
