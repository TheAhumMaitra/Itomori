import Navbar from "@/components/Navbar";
import ShowPreview from "@/components/ShowPreview";
import Installation from "@/components/Installation";
import Footer from "@/components/Footer";
import ASCIILogo from "@/components/ascii_art";

export default function Home() {
  return (
    <>
      <Navbar />
      <ASCIILogo />
      <main>
        <Installation />
        <ShowPreview />
      </main>
      <Footer />
    </>
  );
}
