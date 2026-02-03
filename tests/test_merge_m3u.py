import os
import tempfile
import unittest

from utils.tools import merge_m3u_duplicate_channels


class TestMergeM3U(unittest.TestCase):
    def test_merge_duplicate_channels(self):
        tmpdir = tempfile.mkdtemp()
        path = os.path.join(tmpdir, "test_result.m3u")
        content = (
            "#EXTM3U\n"
            "#EXTINF:-1 tvg-name=\"CCTV-1\" tvg-logo=\"http://logo/CCTV-1.png\",CCTV-1\n"
            "http://a.example/CCTV1.m3u8\n"
            "#EXTINF:-1 tvg-name=\"CCTV-1\" tvg-logo=\"http://logo/CCTV-1.png\",CCTV-1\n"
            "http://b.example/CCTV1.m3u8\n"
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        merge_m3u_duplicate_channels(path)

        with open(path, "r", encoding="utf-8") as f:
            out = f.read()

        expected = (
            "#EXTM3U\n"
            "#EXTINF:-1 tvg-name=\"CCTV-1\" tvg-logo=\"http://logo/CCTV-1.png\",CCTV-1\n"
            "http://a.example/CCTV1.m3u8#http://b.example/CCTV1.m3u8\n"
        )
        self.assertEqual(out, expected)


if __name__ == "__main__":
    unittest.main()
