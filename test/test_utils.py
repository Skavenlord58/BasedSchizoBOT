import unittest


class TestMessageProcessing(unittest.IsolatedAsyncioTestCase):
    async def test_extract_kdo_from_jsem(self):
        m = Message(content="jsem programátor.")
        kdo = " ".join(m.content.split("jsem")[1].split(".")[0].split(",")[0].split(" ")[1:])
        self.assertEqual(kdo, "programátor")

    async def test_extract_kdo_from_jsem_with_comma(self):
        m = Message(content="jsem, programátor.")
        kdo = " ".join(m.content.split("jsem")[1].split(".")[0].split(",")[0].split(" ")[1:])
        self.assertEqual(kdo, "")

    async def test_extract_kdo_from_jsem_with_multiple_words(self):
        m = Message(content="jsem velmi dobrý programátor.")
        kdo = " ".join(m.content.split("jsem")[1].split(".")[0].split(",")[0].split(" ")[1:])
        self.assertEqual(kdo, "velmi dobrý programátor")

    async def test_extract_kdo_from_jsem_with_no_space(self):
        m = Message(content="jsemprogramátor.")
        kdo = " ".join(m.content.split("jsem")[1].split(".")[0].split(",")[0].split(" ")[1:])
        self.assertEqual(kdo, "programátor")

    async def test_extract_kdo_from_jsem_with_no_period(self):
        m = Message(content="jsem programátor")
        kdo = " ".join(m.content.split("jsem")[1].split(".")[0].split(",")[0].split(" ")[1:])
        self.assertEqual(kdo, "programátor")
