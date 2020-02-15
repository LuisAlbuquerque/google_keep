#!/usr/bin/env python3

import gkeepapi
import sys

""" dont autenticate """
if(len(sys.argv) <3):
    print("please call command with <email> <password> of your google keep")
    exit(0)

class GOOGLE_Keep():
    def get_all_notes(keep):
        for note in keep.all():
            print(f"---{note.title}---")
            print(note)

    def get_all_notes_json(keep):
        print("[")
        for note in keep.all():
            print('\t{')
            print(f'\t\t"title": "{note.title}"')
            print(f'\t\t"deleted": "{note.deleted}"')
            print(f'\t\t"note": "{str(note)}"')
            print('\t}')
        print("]")

    def get_by_title(keep,title):
        res_list = keep.find(func=lambda x: x.title == title)
        print(str(res_list.items))


def main():
    email, password = sys.argv[1], sys.argv[2]
    keep = gkeepapi.Keep()
    keep.login(email, password)
    GOOGLE_Keep.get_all_notes_json(keep)

if __name__ == "__main__":
    main()
