import requests


def get_data(endpoint):
    r = requests.get(endpoint)

    if r.status_code == 200:
        if r.headers['content-type'] == 'application/json':
            data = r.json()
            return {"Success": data}
        else:
            return {"Error": f"Content type not json, but {r.headers['content-type']}"}
    else:
        return {"Error": f"{r.status_code}\n{r.text}"}


if __name__ == "__main__":
    endpoint = input()
    print(get_data(endpoint=endpoint))

