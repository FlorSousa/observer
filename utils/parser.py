import argparse
import platform

def parser_args():
    parser = argparse.ArgumentParser(
        description='Tracks mice.'
    )

    parser.add_argument(
        '--project_path', type=str,help=''
    )
    
    return parser.parse_args()

def get_path(args,log_type):
    path = args.video.split('\\')[-1].split('.')[0] if platform.system() == "Windows" else f"./logs/{args.video.split('/')[-1].split('.')[0]}"
    return "./logs/{}_{}.csv".format(path,log_type)