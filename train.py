import argparse

from trains import attention_scn, pure_attention, pure_scn, tagger

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='[(S)how (A)ttend (T)ell - (S)emantic (C)ompositional (N)etworks] - Train Script')

    parser.add_argument('--type', '-t', help='train model type')
    args = parser.parse_args()

    if args.type == 'pure_scn':
        pure_scn.main()
    elif args.type == 'attention_scn':
        attention_scn.main()
    elif args.type == 'pure_attention':
        pure_attention.main()
    else:
        tagger.main()
