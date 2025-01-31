import yayarl

# Don't check the actual behavior but make sure that calls are allowed


def teardown_module():
    yayarl.cache_configure()


def test_cache_clear() -> None:
    yayarl.cache_clear()


def test_cache_info() -> None:
    info = yayarl.cache_info()
    assert info.keys() == {"idna_encode", "idna_decode"}


def test_cache_configure_default() -> None:
    yayarl.cache_configure()


def test_cache_configure_None() -> None:
    yayarl.cache_configure(idna_encode_size=None, idna_decode_size=None)


def test_cache_configure_explicit() -> None:
    yayarl.cache_configure(idna_encode_size=128, idna_decode_size=128)
