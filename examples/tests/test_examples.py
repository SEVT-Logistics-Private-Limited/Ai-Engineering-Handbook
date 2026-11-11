"""Smoke tests: every example runs and produces the results the documentation describes.

Run from the repository root:
    pytest examples/tests -q
"""

import importlib.util
from pathlib import Path

import numpy as np
import pytest

EXAMPLES = Path(__file__).resolve().parents[1]


def load(relative_path: str):
    path = EXAMPLES / relative_path
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_binary_and_bytes():
    m = load("computing_foundations/binary_and_bytes.py")
    assert m.to_binary(4, 4) == "0100"
    assert m.from_binary("11001010") == 202
    with pytest.raises(ValueError):
        m.from_binary("102")
    result = m.main()
    assert result["telugu_bytes"] == 3
    assert result["image_bytes"] == 1920 * 1080 * 3


def test_training_loop_learns_the_line():
    result = load("ai_fundamentals/training_loop.py").main()
    assert result["steps_per_epoch"] == 10
    assert abs(result["w"] - 3) < 0.05 and abs(result["b"] - 2) < 0.05
    assert result["history"][-1] < result["history"][0]


def test_tokenizers():
    m = load("language_models/tokenizer.py")
    tok = m.CharTokenizer("hello")
    assert tok.decode(tok.encode("hell")) == "hell"
    result = m.main()
    assert result["unseen_ids"][2] == 0  # unknown word maps to <unk>


def test_embeddings_similarity():
    m = load("language_models/embeddings_similarity.py")
    result = m.main()
    assert result["car"][0][0] == "vehicle"
    assert result["banana"][0][0] == "apple"


def test_self_attention_is_causal_and_normalized():
    m = load("language_models/self_attention.py")
    weights = m.main()["weights"]
    assert np.allclose(weights.sum(axis=-1), 1.0)
    assert np.allclose(np.triu(weights, k=1), 0.0)


def test_temperature_controls_randomness():
    m = load("language_models/text_generation.py")
    e = m.main()["entropies"]
    assert e[0.3] < e[1.0] < e[2.0]
    with pytest.raises(ValueError):
        m.apply_temperature(np.array([1.0, 2.0]), 0)


def test_prompt_templates():
    prompts = load("language_models/prompt_templates.py").main()
    assert prompts["zero-shot"].count("Answer:") == 1
    assert prompts["few-shot"].count("Answer:") == 3
    assert prompts["role"][0]["role"] == "system"


def test_rag_pipeline_retrieves_the_right_document():
    m = load("language_models/rag_pipeline.py")
    assert len(m.chunk_text(" ".join(str(i) for i in range(50)), chunk_size=20, overlap=5)) == 3
    result = m.main()
    assert result["top_source"] == "engine-manual.txt"
    assert result["precision"] == 1.0 and result["recall"] == 1.0


def test_image_as_array():
    m = load("computer_vision/image_as_array.py")
    result = m.main()
    assert result["shape"] == (2, 4, 3)
    assert result["gray"][0, 3] == 255 and result["gray"][1, 0] == 0


def test_video_as_frames():
    result = load("computer_vision/video_as_frames.py").main()
    assert result["shape"][0] == 30
    assert result["per_min"] == 1920 * 1080 * 3 * 30 * 60


def test_image_patches():
    result = load("computer_vision/image_patches.py").main()
    assert result["patches"] == (196, 768)


def test_rest_api():
    pytest.importorskip("fastapi")
    pytest.importorskip("httpx")
    codes = load("apis/rest_api.py").main()["codes"]
    assert codes == [201, 200, 200, 200, 204, 404, 422]
