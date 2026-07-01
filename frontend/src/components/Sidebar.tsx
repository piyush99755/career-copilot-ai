import { NavLink } from "react-router-dom";

const Sidebar = () => {
  return (
    <aside className="w-64 bg-slate-900 text-white p-6">
      <h1 className="text-2xl font-bold mb-8">
        Career Copilot AI
      </h1>

      <nav className="space-y-3">
        <NavLink
          to="/"
          end
          className={({ isActive }) =>
            `block rounded-lg px-4 py-2 transition ${
              isActive
                ? "bg-blue-600"
                : "hover:bg-slate-700"
            }`
          }
        >
          Dashboard
        </NavLink>

        <NavLink
          to="/history"
          className={({ isActive }) =>
            `block rounded-lg px-4 py-2 transition ${
              isActive
                ? "bg-blue-600"
                : "hover:bg-slate-700"
            }`
          }
        >
          History
        </NavLink>

        <NavLink
          to="/resume"
          className={({ isActive }) =>
            `block rounded-lg px-4 py-2 transition ${
              isActive
                ? "bg-blue-600"
                : "hover:bg-slate-700"
            }`
          }
        >
          Resume
        </NavLink>

        <NavLink
          to="/resume-match"
          className={({ isActive }) =>
            `block rounded-lg px-4 py-2 transition ${
              isActive
                ? "bg-blue-600"
                : "hover:bg-slate-700"
            }`
          }
        >
          Resume Match
        </NavLink>

        <NavLink
        to="/career-chat"
        className={({ isActive }) =>
          `block rounded-lg px-4 py-2 transition ${
            isActive
              ? "bg-blue-600"
              : "hover:bg-slate-700"
          }`
        }
      >
        Career Chat
      </NavLink>


      </nav>
    </aside>
  );
};

export default Sidebar;