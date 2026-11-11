"""A minimal REST API with FastAPI: GET, POST, PUT and DELETE on an in-memory resource.

Run the server:
    uvicorn examples.apis.rest_api:app --reload
    # then open http://127.0.0.1:8000/docs

Or run the built-in demo, which calls every endpoint through a test client:
    python examples/apis/rest_api.py
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Notes API", version="1.0")


class NoteIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    body: str = Field(default="", max_length=2000)


class Note(NoteIn):
    id: int


_notes: dict[int, Note] = {}
_next_id = 1


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/notes")
def list_notes() -> list[Note]:
    return list(_notes.values())


@app.get("/notes/{note_id}")
def get_note(note_id: int) -> Note:
    if note_id not in _notes:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "note not found")
    return _notes[note_id]


@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(note: NoteIn) -> Note:
    global _next_id
    created = Note(id=_next_id, **note.model_dump())
    _notes[_next_id] = created
    _next_id += 1
    return created


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteIn) -> Note:
    if note_id not in _notes:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "note not found")
    _notes[note_id] = Note(id=note_id, **note.model_dump())
    return _notes[note_id]


@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int) -> None:
    if _notes.pop(note_id, None) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "note not found")


def main() -> dict:
    from fastapi.testclient import TestClient

    client = TestClient(app)
    calls = [
        ("POST", "/notes", {"title": "RAG", "body": "Retrieve, augment, generate"}),
        ("GET", "/notes/1", None),
        ("PUT", "/notes/1", {"title": "RAG", "body": "Retrieval-Augmented Generation"}),
        ("GET", "/notes", None),
        ("DELETE", "/notes/1", None),
        ("GET", "/notes/1", None),
        ("POST", "/notes", {"title": ""}),  # fails validation
    ]
    codes = []
    for method, path, body in calls:
        r = client.request(method, path, json=body)
        codes.append(r.status_code)
        print(f"{method:<6} {path:<10} -> {r.status_code} {r.text if r.content else ''}")
    return {"codes": codes}


if __name__ == "__main__":
    main()
