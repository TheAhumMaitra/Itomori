//  SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com

//  SPDX-License-Identifier: 	GPL-3.0-or-later

"use client";

import { CopyButton } from "./ui/shadcn-io/copy-button";

export default function Installation() {
  let uv_url = "uv tool install git+https://github.com/TheAhumMaitra/Itomori.git";

  let pip_url = "pip install Itomori";

  return (
    <>
    <div className="p-3 border-4 rounded-2xl mt-3 border-primary w-full h-full">
      <h1 className="underline text-primary-foreground font-extrabold text-center! text-3xl font-mono">Installation</h1>

    <div className="h-[50vh] flex flex-col justify-center gap-3 items-center mt-4 border-accent border-8 rounded-3xl">
      <h2 className="text-2xl font-bold underline font-mono!">
        Install using uv in Windows or Linux or Mac OS or others:
      </h2>

      <div className="text-1xl p-3 font-bold cursor-pointer! flex gap-3">
        <span className="p-3 rounded-3xl bg-card flex gap-3 text-center justify-center items-center">
        <h3>{uv_url}</h3>
        <CopyButton content={uv_url} variant="default" size="md" />
        </span>

      </div>
    </div>

    <div className="h-[50vh] rounded-3xl flex flex-col justify-center gap-3 items-center mt-4 border-accent border-8">
      <h2 className="text-2xl font-bold underline font-mono!">
        Install using pip in Windows or Linux or Mac OS or others:
      </h2>

      <div className="text-1xl p-3 font-bold cursor-pointer! flex gap-3">
        <span className="p-3 rounded-3xl bg-card flex gap-3 text-center justify-center items-center">
        <h3>{pip_url}</h3>
        <CopyButton content={pip_url} variant="default" size="md" />
        </span>

      </div>
    </div>
    </div>
    </>
  );
}
