#!/usr/bin/env python3
import os
import unittest

from book_tester import ChapterTest


class Chapter20Test(ChapterTest):
    chapter_name = "chapter_21_mocking_2"
    previous_chapter = "chapter_20_mocking_1"

    def test_listings_and_commands_and_output(self):
        self.parse_listings()
        self.start_with_checkout()

        # sanity checks
        self.assertEqual(self.listings[0].type, "code listing with git ref")
        self.assertEqual(self.listings[1].type, "code listing")
        self.assertEqual(self.listings[1].skip, True)
        self.assertEqual(self.listings[2].type, "code listing with git ref")

        # skips
        # self.skip_with_check(22, 'switch back to master') # comment

        self.prep_database()
        # self.sourcetree.run_command("rm src/accounts/tests.py")
        self.sourcetree.run_command("mkdir -p src/static")

        # hack fast-forward
        if os.environ.get("SKIP"):
            self.pos = 75
            self.sourcetree.run_command(
                "git switch {}".format(self.sourcetree.get_commit_spec("ch19l037"))
            )

        while self.pos < len(self.listings):
            print(self.pos)
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)
        self.check_final_diff(ignore=["moves"])


if __name__ == "__main__":
    unittest.main()
