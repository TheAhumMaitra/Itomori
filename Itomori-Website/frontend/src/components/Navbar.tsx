//  SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com

//  SPDX-License-Identifier: 	GPL-3.0-or-later


import Link from "next/link";
import { FaGithub } from "react-icons/fa";

import { Alert, AlertTitle } from "@/components/ui/alert";
import { ModeToggle } from "./theme-toggle";
import Image from "next/image";

export default function Navbar() {
  return (
    <>
      <Alert className="mt-1">
        <AlertTitle className="text-chart-3 font-bold w-full h-full text-center">
          <Link
            className="hover:text-destructive"
            href={
              "https://github.com/TheAhumMaitra/Itomori/releases/tag/v1.1.0"
            }
          >
            Itomori v1.1.0 just released!
          </Link>
        </AlertTitle>
      </Alert>

      <nav className="flex mt-4 justify-between p-2.5 items-center h-full sticky top-0 border-4 border-border w-full backdrop-blur-sm rounded-2xl text-foreground">
        <Link
          className="text- font-bold h-full text-center"
          href={"https://github.com/TheAhumMaitra/Itomori"}
        >
          <Image className="bg-transparent m-3 scale-170 rounded-2xl" alt="Logo" src={"/logo.png"} width={100} height={120} />

        </Link>
        <ul>
          <li className=" font-medium text-xl bg-card p-3 rounded-2xl hover:text-primary hover:font-extrabold">
            <Link href={"https://itomoridocs.vercel.app/"}>Docs</Link>
          </li>
        </ul>
        <div className="flex gap-3">
          <Link href={"https://github.com/TheAhumMaitra/Itomori"} className="cursor-pointer">

        <FaGithub size={34}/>
          </Link>
        <ModeToggle />
        </div>
      </nav>
    </>
  );
}
