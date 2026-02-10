//  SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com

//  SPDX-License-Identifier: 	GPL-3.0-or-later

"use client";

import { CopyButton } from "./ui/shadcn-io/copy-button";

export default function Installation() {
  let uv_Git_url = "uv tool install git+https://github.com/TheAhumMaitra/Itomori.git";

  let uv_package_url = "uv tool install Itomori"

  let pipx_url = "pipx install Itomori";

  return (
    <>
    <div className="p-3 border-4 rounded-2xl mt-3 border-primary w-full h-full">
      <h1 className="underline text-primary-foreground font-extrabold text-center! text-3xl font-mono">Installation</h1>

    <div className="h-[50vh] flex flex-col justify-center gap-3 items-center mt-4 border-accent border-8 rounded-3xl">
      <h2 className="text-2xl font-bold underline font-mono!">
        Install Itomori using uv
      </h2>
      <h3 className="text-chart-2 font-medium text-sm">Available for Windows, Linux, Mac OS</h3>

      <div className="text-1xl p-3 font-bold cursor-pointer! flex gap-3">
        <span className="p-3 rounded-3xl bg-card flex gap-3 text-center justify-center items-center">
        <h3>{uv_Git_url}</h3>
        <CopyButton content={uv_Git_url} variant="default" size="md" />
        </span>


      </div>
        <h3>Or (use the package) <span className="text-chart-4">Which is more stable</span></h3>
        <span className="p-3 rounded-3xl bg-card flex gap-3 text-center justify-center items-center">
        <h3>{uv_package_url}</h3>
        <CopyButton content={uv_package_url} variant="default" size="md" />
        </span>

    </div>

    <div className="h-[50vh] rounded-3xl flex flex-col justify-center gap-3 items-center mt-4 border-accent border-8">
      <h2 className="text-2xl font-bold underline font-mono!">
        Install using pipx
      </h2>
      <h3 className="text-chart-2 font-medium text-sm">Available for Windows, Linux, Mac OS</h3>

      <div className="text-1xl p-3 font-bold cursor-pointer! flex gap-3">
        <span className="p-3 rounded-3xl bg-card flex gap-3 text-center justify-center items-center">
        <h3>{pipx_url}</h3>
        <CopyButton content={pipx_url} variant="default" size="md" />
        </span>

      </div>
    </div>
    </div>
    </>
  );
}
