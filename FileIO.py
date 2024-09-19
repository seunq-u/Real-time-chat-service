import orjson, typing

def read_json(path: str) -> typing.Tuple[typing.Union[dict, bool], typing.Union[str, None]]:
    try:
        path = path[1]
        with open(f'{path}', 'rb') as f:
            data = orjson.loads(f.read())
        return (data, )

    except orjson.JSONDecodeError as e:
        print(f"JSONDecodeError: FileIO.read_json: {path}")
        return (False, f"JSONDecodeError: FileIO.read_json: {path}")

    except Exception as e:
        print(f"{e}: FileIO.read_json: {path}")

        return (False, f"{e}: FileIO.read_json: {path}")
