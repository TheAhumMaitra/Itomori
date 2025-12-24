//  SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com

//  SPDX-License-Identifier: 	GPL-3.0-or-later

// import next js link component
import Link from "next/link";

export default function Footer() {
  return (
    <>
    {/* footer  */}
      <footer className="h-full w-full backdrop-blur-sm sticky bottom-0 mt-3 flex flex-col justify-center items-center font-bold p-3">
        <h1>
          {/* inform visiter about - source code license and content license  */}
          This website&apos;s source code is open source and it&apos;s licensed under  <Link
            className="hover:italic hover:text-destructive ml-1"
            href={"https://www.gnu.org/licenses/gpl-3.0.en.html"}
          >
           GPL-3.0
          </Link> and content is licensed under
          <Link
            className="hover:italic hover:text-destructive ml-1"
            href={"https://creativecommons.org/licenses/by-sa/4.0/"}
          >
            CC BY-SA 4.0
          </Link>
        </h1>
      </footer>
    </>
  );
}
