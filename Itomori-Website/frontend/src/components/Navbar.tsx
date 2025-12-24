//  SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com

//  SPDX-License-Identifier: 	GPL-3.0-or-later

// import Link component
import Link from "next/link";

// import Github icon
import { FaGithub } from "react-icons/fa";

// import Shacdn Ui Alert component
import { Alert, AlertTitle } from "@/components/ui/alert";
import { ModeToggle } from "./theme-toggle";

// import Nex JS image component
import Image from "next/image";

// Navbar
export default function Navbar() {
  return (
    <>
    {/* inform about new version  */}
      <Alert className="mt-1">
        <AlertTitle className="text-chart-3 font-bold w-full h-full text-center">
          <Link
            className="hover:text-destructive"
            href={
              "https://github.com/TheAhumMaitra/Itomori/releases/tag/v1.1.1"
            }
          >
            Itomori v1.1.1 just released!
          </Link>
        </AlertTitle>
      </Alert>

      {/* main navbar  */}
      <nav className="flex mt-3 justify-between p-2.5 items-center h-full sticky top-[0.2rem] border-4 border-border w-full backdrop-blur-[1rem] rounded-2xl text-foreground bg-[#ffffff2c]">

        {/* logo  */}
        <Link
          className="text- font-bold h-full text-center"
          href={"https://github.com/TheAhumMaitra/Itomori"}
        >

          <Image className="bg-transparent m-3 scale-170 rounded-2xl" alt="Logo" src={"/logo.png"} width={100} height={120} />

        </Link>
        {/* all links  */}
        <ul className="font-mono">
          {/* Documentation link  */}
          <li className=" font-medium text-xl bg-card p-3 rounded-2xl hover:text-primary hover:font-extrabold">
            <Link href={"https://itomoridocs.vercel.app/"}>Docs</Link>
          </li>
        </ul>
        {/* Github repo link with icon  */}
        <div className="flex gap-3">
          <Link href={"https://github.com/TheAhumMaitra/Itomori"} className="cursor-pointer">

        <FaGithub size={34}/>
          </Link>

        {/* Theme switch button  */}
        <ModeToggle />
        </div>
      </nav>
    </>
  );
}
