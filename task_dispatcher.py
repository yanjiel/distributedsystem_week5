import argparse



def start(mode="local", port="5000", worker=None):
    print(f"mode: {mode}, port: {port}, worker: {worker}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='task dispatcher')
    parser.add_argument('-m', '--mode', type=str, required=True, help='mode of task dispatcher, local/pull/push')
    parser.add_argument('-p', '--port', type=int, required=True, help='port for connection with Redis db')
    parser.add_argument('-w', '--worker', type=int, required=False, help='optional number of workers (local mode only)')

    args = parser.parse_args()

    if args.mode.lower() == "local":
        if not args.worker: raise SyntaxError("must include number of workers with -w when using local mode.")

    start(mode = args.mode, port = args.port, worker = args.worker)

