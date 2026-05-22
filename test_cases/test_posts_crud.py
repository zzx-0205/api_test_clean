import pytest

class TestPostsCRUD:
    @pytest.mark.parametrize("post_id,expected_status", [
        (1, 200),
        (99999, 404)
    ])
    def test_get_post(self, api_client, post_id, expected_status):
        resp = api_client.get(f"/posts/{post_id}")
        assert resp.status_code == expected_status
        if expected_status == 200:
            assert resp.json()["id"] == post_id

    def test_create_post(self, api_client):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        resp = api_client.post("/posts", json=payload)
        assert resp.status_code == 201
        data = resp.json()
        assert data["title"] == "foo"
        assert data["id"] is not None

    def test_update_post(self, api_client):
        payload = {"id": 1, "title": "updated title", "body": "new body", "userId": 1}
        resp = api_client.put("/posts/1", json=payload)
        assert resp.status_code == 200
        assert resp.json()["title"] == "updated title"

    def test_patch_post(self, api_client):
        resp = api_client.patch("/posts/1", json={"title": "patched"})
        assert resp.status_code == 200
        assert resp.json()["title"] == "patched"

    def test_delete_post(self, api_client):
        resp = api_client.delete("/posts/1")
        assert resp.status_code == 200