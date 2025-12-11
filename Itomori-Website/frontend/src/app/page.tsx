import Navbar from "@/components/Navbar";
import ShowPreview from "@/components/ShowPreview";
import Installation from "@/components/Installation";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <>
      <Navbar />
      <main>
        <Installation />
        <ShowPreview />
      </main>
      <Footer />
    </>
  );
}
