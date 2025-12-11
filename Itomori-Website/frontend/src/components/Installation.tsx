"use client";

import { Kbd } from "@/components/ui/kbd";

export default function Installation() {
  const install_command = `curl -sSL "https://raw.githubusercontent.com/TheAhumMaitra/Itomori/refs/heads/main/Linux%20Install%20Scripts/install.sh" | bash`;

  const copy = () => {
    navigator.clipboard.writeText(install_command);
  };

  return (
    <div className="h-[50vh] flex flex-col justify-center gap-3 items-center mt-4 border-accent border-8">
      <h2 className="text-2xl font-bold underline">
        Install using one command in Linux:
      </h2>

      <Kbd className="text-1xl font-bold cursor-pointer!" onClick={copy}>
        {install_command}
      </Kbd>
    </div>
  );
}
