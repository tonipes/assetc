import os

def all_files_in(path):
    files = []
    for r, d, f in os.walk(path):
        files += [os.path.join(r, fi) for fi in f]
    return files

def mkdir(path):
    if path:
        os.makedirs(path, exist_ok=True)

def substitute(inputs=[], **substitutions):
    
    return [i.format(**substitutions) for i in inputs]

def build_main_substitutions(main_source_root_folder, main_target_root_folder, main_staging_root_folder):
    return {
        "main_source_root_folder":      main_source_root_folder,
        "main_staging_root_folder":     main_staging_root_folder,
        "main_target_root_folder":      main_target_root_folder,
    }

def build_substitutes(filepath, source_root_folder, target_root_folder, staging_root_folder):
    source_filepath  = os.path.join(source_root_folder, filepath)
    target_filepath  = os.path.join(target_root_folder, filepath)
    staging_filepath = os.path.join(staging_root_folder, filepath)

    subs = {
        "file_name":                os.path.basename(filepath),
        "file_basename":            os.path.splitext(os.path.basename(filepath))[0],
        "file_extension":           os.path.splitext(os.path.basename(filepath))[1][1:],
        "filepath_relative":        filepath,
        
        "source_filepath_name":     os.path.splitext(source_filepath)[0],
        "target_filepath_name":     os.path.splitext(target_filepath)[0],
        "staging_filepath_name":    os.path.splitext(staging_filepath)[0],

        "source_filepath_dir":      os.path.dirname(source_filepath),
        "target_filepath_dir":      os.path.dirname(target_filepath),
        "staging_filepath_dir":     os.path.dirname(staging_filepath),

        "source_filepath":          source_filepath,
        "target_filepath":          target_filepath,
        "staging_filepath":         staging_filepath,

        "source_root_folder":       source_root_folder,
        "target_root_folder":       target_root_folder,
        "staging_root_folder":      staging_root_folder,
    }
        
    return subs
