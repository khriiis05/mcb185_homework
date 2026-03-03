import argparse

#Positional Arguments
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('size', type=int, help='window size')
parser.add_argument('entropy', type=float, help='entropy threshold')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)

#Named Arguments
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)

#Flags
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

#Short and Long
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)