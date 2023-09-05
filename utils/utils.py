import argparse
import platform

def parser_args():
    parser = argparse.ArgumentParser(
        description='Tracks mice.'
    )

    parser.add_argument(
        '--project_path', type=str,help=''
    )

    parser.add_argument(
        '--video', type=str,
        help='Path to the video file to be processed.'
    )

    parser.add_argument(
        '--frame-rate', type=int,
        help='Frame rate of the video file to be processed.'
    )

    parser.add_argument(
        '--draw-axis', action='store_true',
        help='Draw both PCA axis.'
    )

    parser.add_argument(
        '--save-video', action='store_true',
        help='Create a video file with the analysis result.'
    )

    parser.add_argument(
        '--color-mask', action='store_true',
        help='Draw a colored mask over the detection.'
    )

    parser.add_argument(
        '--log-position', action='store_true',
        help='Logs the position of the center of mass to file.'
    )

    parser.add_argument(
        '--log-speed', action='store_true',
        help='Logs the speed of the center of mass to file.'
    )
    
    return parser.parse_args()

def get_path(args,log_type):
    path = args.video.split('\\')[-1].split('.')[0] if platform.system() == "Windows" else f"./logs/{args.video.split('/')[-1].split('.')[0]}"
    return "./logs/{}_{}.csv".format(path,log_type)