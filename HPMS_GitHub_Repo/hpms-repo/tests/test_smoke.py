from src.hpms import main


def test_main_runs(capsys):
    main.main()
    assert "Hospital Patient Management System" in capsys.readouterr().out
