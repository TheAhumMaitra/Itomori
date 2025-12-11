import Link from "next/link";

import { Alert, AlertTitle } from "@/components/ui/alert";
import { ModeToggle } from "./theme-toggle";

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

      <nav className="flex mt-4 p-3 justify-between items-center h-full sticky top-0 border-4 border-border w-full backdrop-blur-sm rounded-2xl text-foreground">
        <Link
          className="text-2xl font-bold w-full h-full text-center"
          href={"https://github.com/TheAhumMaitra/Itomori"}
        >
          Itomori
        </Link>
        <ul>
          <li className="mr-4 hover:text-purple-700 hover:font-extrabold">
            <Link href={"https://itomoridocs.vercel.app/"}>Docs</Link>
          </li>
        </ul>
        <ModeToggle />
      </nav>
    </>
  );
}
