from __future__ import absolute_import

from mypkg import transform


def test_text():
    assert(transform.text.strip() == "strip")


def test_video():   
    assert(transform.video.cut() == "cut")


def test_audio():
    assert(transform.audio.transform() == "squeeze")
