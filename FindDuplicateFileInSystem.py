"""
    LeetCode: 609 Find Duplication File in System
"""

from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        duplicate_groups = {}
        for path in paths:

            # Extract the directory path first
            folder_path = path.split(" ")[0]
            documents = path.split(" ")[1:]

            # Iterate over the documents
            for doc in documents:

                # Extract document name and content
                # Ideally Regex would be cleaner implementation
                doc_name, content = doc.split("(")
                content = content[:-1]
                full_path = f"{folder_path}/{doc_name}"

                if duplicate_groups.get(content):
                    duplicate_groups[content].append(full_path)
                else:
                    duplicate_groups[content] = [full_path]
        result = []
        for group in duplicate_groups.values():
            if len(group) > 1:
                result.append(group)

        return result


if __name__ == "__main__":

    solution = Solution()

    system_a = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)",
    ]

    assert solution.findDuplicate(system_a) == [
        ["root/a/1.txt", "root/c/3.txt"],
        ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
    ]

    system_b = [
        "root/a 1.txt(abcd) 2.txt(efsfgh)",
        "root/c 3.txt(abdfcd)",
        "root/c/d 4.txt(efggdfh)",
    ]
    assert solution.findDuplicate(system_b) == []

    system_c = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
    ]
    assert solution.findDuplicate(system_c) == [
        ["root/a/1.txt", "root/c/3.txt"],
        ["root/a/2.txt", "root/c/d/4.txt"],
    ]
